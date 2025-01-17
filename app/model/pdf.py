from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, TableStyle, Paragraph, Table

from app import data
from app.model import Order
from app.model.orm import MaterialData

pdfmetrics.registerFont(TTFont("OpenSans", 'font/OpenSans.ttf'))
pdfmetrics.registerFont(TTFont("OpenSansBold", 'font/OpenSans-Bold.ttf'))

col_width = lambda *k, width=(A4[0] - data.MARGIN * 2): [width * k_ for k_ in k]
P = Paragraph


def create_assigment_doc(order: Order, need_scheme: bool):
    pdf_path = f'documents\\Наряд_{order.id}.pdf'
    pdf = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=data.MARGIN,
        rightMargin=data.MARGIN,
        topMargin=data.MARGIN,
        bottomMargin=data.MARGIN
    )

    h_l_style = ParagraphStyle('', fontName='OpenSans', fontSize=data.H_FONT_SIZE, leading=data.H_LENDING)
    h_r_style = ParagraphStyle('', fontName='OpenSansBold', fontSize=data.H_FONT_SIZE, leading=data.H_LENDING,
                               alignment=TA_RIGHT)

    p_default_style = ParagraphStyle('', fontName='OpenSans', fontSize=data.P_FONT_SIZE, spaceAfter=data.SPACE_AFTER,
                                     leading=data.P_LENDING)
    p_bold_style = ParagraphStyle('', fontName='OpenSansBold', fontSize=data.P_FONT_SIZE, spaceAfter=data.SPACE_AFTER,
                                  leading=data.P_LENDING)

    fragments = [fragment for door in order.doors for fragment in door.fragments if not fragment.fragment_container]

    if order.is_2_line is not None:
        guide = (f"Верхняя {(lc := 'двуполозная' if order.is_2_line else 'однополозная')}"
                 f" направляющая: {(gl := order.guide_long if order.guide_long else order.doorway_width)}<br/>"
                 f"Нижняя {lc} направляющая: {gl}<br/>")
    else:
        guide = ''

    sorted_horizonts = {}
    for door in order.doors:
        horizont = door.width - order.profile.v_width * 2
        if sorted_horizonts.get(horizont) is None:
            sorted_horizonts[horizont] = 1
        else:
            sorted_horizonts[horizont] += 1
    horizonts = ' '.join(
        (f'{int(horizont) if horizont.is_integer() else horizont}-{count}шт.'
         for horizont, count in sorted_horizonts.items())
    )

    sorted_profiles = {}
    for door in order.doors:
        door_profile = door.height
        if sorted_profiles.get(door_profile) is None:
            sorted_profiles[door_profile] = 1
        else:
            sorted_profiles[door_profile] += 1
    profiles = ', '.join(f'{int(profile) if profile.is_integer() else profile}-{count * 2}шт'
                         for profile, count in sorted_profiles.items())

    shlegel = int((order.doorway_height - order.profile.guide) * len(order.doors) * 2 + 5) if order.need_shlegel else ''
    sealant = int(s) + 10 if (s := sum(((fragment.height + fragment.visible_width) * 2
                                        for fragment in fragments if
                                        not fragment.fragment_container and fragment.is_have_sealant))) else ''

    story = [
        Table(  # header
            data=[[
                Paragraph(f"{data.COMPANY_NAME}<br/>{data.ADDRESS}<br/>{data.PHONE}", style=h_l_style),
                Paragraph(f"Наряд №{order.visible_number} {order.profile.name}", style=h_l_style),
                Paragraph(
                    f"{order.delivery_config_name}<br/>{order.set_config_name}<br/>{order.pack_config_name}",
                    style=h_r_style)
            ]],
            spaceAfter=data.SPACE_AFTER,
            colWidths=col_width(.5, .2, .3)
        ),
        Paragraph(  # doors
            f"{', '.join(str(int(door.width)) for door in order.doors)}",
            p_bold_style
        ),
        Table(  # order info
            data=[[
                Paragraph(
                    f"Покупатель: {order.customer.name}<br/>"
                    f"Ответственный: {order.responsible.name}<br/>"
                    f"Тел: {order.responsible.phone}",
                    style=h_l_style
                ),
                Paragraph(
                    f"Цвет профиля: {order.color.name}<br/>"
                    f"Дата создания: {order.create_date.strftime('%d.%m.%Y')}<br/>"
                    f"Дата готовности: {order.out_date.strftime('%d.%m.%Y')}",
                    style=h_l_style
                )
            ]],
            rowHeights=None,
            spaceAfter=data.SPACE_AFTER,
            colWidths=col_width(.5, .5)
        ),
        Paragraph(  # other products
            f"{guide}"
            f"Горизонтальный верхний: {horizonts}<br/>"
            f"Горизонтальный нижний: {horizonts}<br/>"
            f"Ригель {order.rigel.name}: "
            f"{', '.join(f'{size}-{count}шт.' for size, count in order.grouped_rigels.items())}<br/>"
            f"Вертикальный {'открытый' if order.profile.is_open else 'закрытый'}: {profiles}<br/>"
            f"Ролик верхний: {len(order.doors)}<br/>"
            f"Ролик нижний: {len(order.doors)}<br/>"
            f"Шлегель: {shlegel}<br/>"
            f"Уплотнитель: {sealant}",
            style=p_default_style,
        ),
        Paragraph(
            '<br/>'.join(f"{material}: {', '.join(f'(№{n}, {y}x{x})-{c}шт' for (y, x), (c, n) in fragments.items())}"
                         for material, fragments in order.group_fragments().items()),
            style=p_default_style
        ),
        Paragraph(
            f"{order.additional_materials}",
            style=p_bold_style
        )
    ]

    copy = story.copy()
    pdf.build(story)

    if need_scheme:
        pdf.build(copy, canvasmaker=lambda *_, **__: draw_scheme(
            filename=pdf_path,
            pagesize=A4,
            order=order,
            ph=sum(map(lambda i: i.height if isinstance(i, Paragraph) else sum(i._rowHeights), copy)) + 10 * len(copy),
            fragments_info=False,
        ))

    return pdf_path


def create_scheme_doc(order: Order):
    pdf_path = f'documents\\Рисунок_{order.id}.pdf'
    a4_formate = tuple(reversed(A4)) if (sum(door.width for door in order.doors) * 1.1 >
                                         order.doorway_height - order.profile.guide) else A4

    SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=data.MARGIN,
        rightMargin=data.MARGIN,
        topMargin=data.MARGIN,
        bottomMargin=data.MARGIN
    ).build([], canvasmaker=lambda *_, **__: draw_scheme(
        filename=pdf_path,
        pagesize=a4_formate,
        order=order,
        ph=0,
        fragments_info=True,
    ))

    return pdf_path


def create_material_doc(order: Order, is_for_glass: bool, *materials: MaterialData):
    pdf_path = f'documents\\заявка_{int(is_for_glass)}_{order.id}.pdf'
    fragments = order.group_fragments()

    h_style = ParagraphStyle('', fontName='OpenSansBold', fontSize=data.MD_FONT_SIZE, leading=data.MD_LENDING,
                             spaceAfter=data.SPACE_AFTER)
    tp = ParagraphStyle('', fontName='OpenSansBold', fontSize=data.MD_TABLE_FONT_SIZE, leading=data.MD_TABLE_LENDING)

    material_data: list[list] = [['Вид работы', '№', 'Высота', 'Ширина', 'К-во']]
    material_spans: list[list] = []
    row = 1
    for material in materials:
        for i, ((h, w), (count, n)) in enumerate(fragments[material.name].items()):
            material_data.append([P(material.name, tp), P(str(n), tp), P(str(h), tp), P(str(w), tp), P(str(count), tp)])
            if i == 1:
                material_data[row][0] = ''
                material_spans.append(['SPAN', (0, row - 1), (0, row)])
            elif i > 1:
                material_data[row][0] = ''
                material_spans[-1][-1] = (0, row)
            row += 1

    th_style = [
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'OpenSans'),
        ('FONTSIZE', (0, 0), (-1, -1), data.MD_FONT_SIZE),
        ('LEADING', (0, 0), (-1, -1), data.MD_LENDING),
    ]

    st_style = [
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'OpenSans'),
        ('FONTSIZE', (0, 0), (-1, -1), data.MD_FONT_SIZE),
        ('LEADING', (0, 0), (-1, -1), data.MD_LENDING),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('GRID', (0, 0), (-1, -1), 0, colors.black),
    ]

    SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=data.MARGIN,
        rightMargin=data.MARGIN,
        topMargin=data.MARGIN,
        bottomMargin=data.MARGIN
    ).build([
        Paragraph(f"Заявка №{order.visible_number} - {order.set_config_name}", h_style),
        Table(
            data=[
                [f"Отвественный: {order.responsible.name}", f"Покупатель: {order.customer.name}"],
                [f"Тел: {order.responsible.phone}", f"Дата готовности: {order.out_date}"]
            ],
            colWidths=col_width(.5, .5),
            style=TableStyle(th_style),
            spaceAfter=data.SPACE_AFTER
        ),
        Table(
            data=material_data,
            colWidths=col_width(.5, .07, .18, .18, .07),
            rowHeights=None,
            style=TableStyle(st_style + material_spans)
        )
    ])
    return pdf_path


def draw_scheme(filename: str, pagesize: tuple, order: Order, ph: int, fragments_info: bool, door_spacing=.1):
    fragment_ps = ParagraphStyle('', fontName='OpenSans', fontSize=10, spaceAfter=0)
    c = Canvas(filename, pagesize=pagesize)

    width, height = pagesize
    pos_x_start = width - data.MARGIN
    pos_y_start = height - ph - data.MARGIN
    page_width = pos_x_start - data.MARGIN
    page_height = pos_y_start - data.MARGIN

    scheme_width = sum(door.width for door in order.doors) * (1 + door_spacing)
    scheme_height = order.doorway_height - order.profile.guide

    if scheme_width * (scale := page_height / scheme_height) > page_width:
        scale = page_width / scheme_width

    door_spacing = scheme_width / len(order.doors) * door_spacing * scale
    fragment_spacing = order.rigel.center_width * scale

    pos_x = data.MARGIN * 1.5
    for door in order.doors:
        cols = door.cols
        rows = door.rows
        for fragment in door.fragments:
            if not fragment.fragment_container:
                x = pos_x + sum(cols[:fragment.x]) * scale + fragment_spacing * (fragment.x - 1)
                y = pos_y_start - (sum(rows[:fragment.y]) * scale + fragment.height * scale
                                   + fragment_spacing * (fragment.y - 1))
                w = fragment.width * scale
                h = fragment.height * scale
                text = f"{fragment.number_in_scheme}"
                if fragments_info:
                    text += f" ({fragment.visible_height}x{fragment.visible_width} {fragment.material_name})"
                c.setFillColor(colors.Color(233 / 255, 233 / 255, 233 / 255))
                c.rect(x, y, w, h, fill=not fragment.is_have_sealant)
                c.setFillColor('black')
                try:
                    p = Paragraph(text, fragment_ps)
                    p.wrapOn(c, w - 10, h - 10)
                    p.drawOn(c, x + 5, y + h - 5 - p.height)
                except:
                    pass
        pos_x += door.width * scale + door_spacing

    return c
