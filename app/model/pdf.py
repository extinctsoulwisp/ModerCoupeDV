from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, TableStyle, Paragraph, Table, Image

from app import data
from app.model import Order
from app.model.one_c import OneCNomenclature
from app.model.orm import MaterialData, Database

pdfmetrics.registerFont(TTFont("OpenSans", 'font/OpenSans.ttf'))
pdfmetrics.registerFont(TTFont("OpenSansBold", 'font/OpenSans-Bold.ttf'))

col_width = lambda *k, width=(A4[0] - data.MARGIN * 2): [width * k_ for k_ in k]
P = Paragraph


def num_to_str(num: int | float | None):
    if num is None:
        return ""
    num = float(num)
    if num.is_integer():
        num = int(num)
    else:
        num = round(num, 2)
    print(num)
    return "" if num is None else f"{num:_}".replace('.', ',').replace('_', ' ')


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
        if order.quide_decor is not None:
            guide = (
                f"Верхний ходовой: {(gl := order.guide_long if order.guide_long else order.doorway_width)}"
                f"-{2 if order.is_2_line else 1}шт.<br/>"
            )
            if order.quide_decor:
                guide += f"Накладка на направляющую: {gl}-{order.quide_decor}шт.<br/>"
        else:
            guide = (
                f"Верхняя {(lc := 'двуполозная' if order.is_2_line else 'однополозная')}"
                f" направляющая: {(gl := order.guide_long if order.guide_long else order.doorway_width)}<br/>"
                f"Нижняя {lc} направляющая: {gl}<br/>"
            )
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
        # noinspection PyTypeChecker
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

    # noinspection PyTypeChecker
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
    p = ParagraphStyle('', fontName='OpenSans', fontSize=data.MD_FONT_SIZE, leading=data.MD_LENDING)

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
                [P(f"Отвественный: {order.responsible.name}", p), P(f"Покупатель: {order.customer.name}", p)],
                [P(f"Тел: {order.responsible.phone}", p), P(f"Дата готовности: {order.out_date}", p)]
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


def draw_scheme(filename: str, pagesize: tuple, order: Order, ph: int, fragments_info: bool, door_spacing=.1,
                _pos_y_start=None, full_page_width=None, fragments_numbers=True):
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

    if full_page_width is not None:
        print(f"Adjusting scheme width to fit full page width: {full_page_width}", scheme_width * scale)
        pos_x = full_page_width - data.MARGIN * 1.5 - scheme_width * scale
    else:
        pos_x = data.MARGIN * 1.5

    if _pos_y_start is not None:
        pos_y_start = _pos_y_start
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
                text = ""
                if fragments_numbers:
                    text += f"{fragment.number_in_scheme}"
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


def create_customer_doc(order: Order):
    pdf_path = f'documents\\Заказ_покупателя_{order.id}.pdf'

    h_style = ParagraphStyle('', fontName='OpenSansBold', fontSize=data.MD_FONT_SIZE, leading=data.MD_LENDING,
                             spaceAfter=data.SPACE_AFTER)
    h_c_style = ParagraphStyle('', fontName='OpenSansBold', fontSize=data.MD_FONT_SIZE, leading=data.MD_LENDING,
                               spaceAfter=data.SPACE_AFTER, alignment=TA_CENTER)
    h_r_style = ParagraphStyle('', fontName='OpenSansBold', fontSize=data.H_FONT_SIZE, leading=data.H_LENDING,
                               alignment=TA_RIGHT)
    p_bold_style = ParagraphStyle('', fontName='OpenSansBold', fontSize=data.P_FONT_SIZE, leading=data.P_LENDING)
    p_c_bold_style = ParagraphStyle('', fontName='OpenSansBold', fontSize=data.P_FONT_SIZE, leading=data.P_LENDING,
                                    alignment=TA_CENTER)
    tp = ParagraphStyle('', fontName='OpenSansBold', fontSize=data.MD_TABLE_FONT_SIZE, leading=data.MD_TABLE_LENDING)
    p = ParagraphStyle('', fontName='OpenSans', fontSize=data.P_FONT_SIZE, leading=data.MD_LENDING)
    p_r_style = ParagraphStyle('', fontName='OpenSans', fontSize=data.P_FONT_SIZE, leading=data.MD_LENDING,
                               alignment=TA_RIGHT)

    pdf = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=data.MARGIN,
        rightMargin=data.MARGIN,
        topMargin=data.MARGIN,
        bottomMargin=data.MARGIN
    )

    materials = [
        (OneCNomenclature('', 'Серебро Верхняя 2-х полоз. направляющая 5,9м', 389, 'м'), 1.6),
        (OneCNomenclature('', 'Серебро Нижняя 2-х полоз. направляющая 5,9м', 220, 'м'), 1.6),
        (OneCNomenclature('', 'Серебро Горизонт.профиль верхний 5,9м', 176, 'м'), 1.6),
        (OneCNomenclature('', 'Серебро Горизонт.профиль нижний 5,9м', 389, 'м'), 1.6),
        (OneCNomenclature('', 'Серебро Ригель 5,9м', 188, 'м'), 3.2),
        (OneCNomenclature('', 'Серебро Вертикал.профиль открытый 5,9м', 1433, 'шт'), 2),
        (OneCNomenclature('', 'К-т роликов СН-01 ОРК асим.верх подшипник 6*35', 250, 'компл'), 2),
        (OneCNomenclature('', 'Шлегель 7*6 серебро', 15, 'м'), 10),
        (OneCNomenclature('', 'Стопор платиковый (Серый)', 25, 'шт'), 2),
    ]

    services = [
        (OneCNomenclature('', 'Нарезка профиля в размер', 15, 'шт'), 14),
        (OneCNomenclature('', 'Сверление отверстий в профиле', 15, 'шт'), 12),
        (OneCNomenclature('', 'Упаковка профиля', 60, 'шт'), 1),
    ]

    story = [
        t1 := Table(  # header
            data=[[
                Image('icons/logo_min.png', width=269, height=48),
                Paragraph(f"{data.COMPANY_NAME}<br/>{data.ADDRESS}<br/>{data.PHONE}", style=p_r_style),
            ]],
            spaceAfter=data.SPACE_AFTER,
            colWidths=col_width(.2, .8),
            style=TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ])
        ),
        p2 := Paragraph(f'Заказ-наряд покупателя №{order.visible_number}', h_c_style),
        Table(  # header
            data=[[p3 := Paragraph(
                f"Дата создания: {order.create_date.strftime('%d.%m.%Y')}<br/>"
                f"Покупатель: {order.customer.name}<br/>"
                f"Отвественный: {order.responsible.name}<br/>"
                f"Профиль: {order.profile.name}<br/>"
                f"Цвет: {order.color.name}<br/>"
                f"Кол-во дверей: {order.door_count}<br/>",
                style=p
            ), '']],
            spaceAfter=data.SPACE_AFTER
        ),
        Table(
            data=[
                [P(text, p_c_bold_style) for text in ('№', 'Материалы', 'Ед.', 'Цена', 'Кол-во', 'Стоимость')],
                *(
                    [P(t, p) for t in (
                        str(i + 1), m.name, m.unit, num_to_str(m.price), num_to_str(count), num_to_str(m.price * count)
                    )]
                    for i, (m, count) in enumerate(materials)
                ),
                [P('Общая стоимость:', p_r_style), '', '', '', '',
                 P(num_to_str(m_total := sum(m.price * count for m, count in materials)), p)],
            ],
            style=[
                ('GRID', (0, 0), (-1, -1), 0, colors.black),
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(233 / 255, 233 / 255, 233 / 255)),
                ('SPAN', (0, -1), (-2, -1)),
            ],

            colWidths=col_width(.05, .44, .1, .11, .12, .17),
            spaceAfter=data.SPACE_AFTER,
        ),
        Table(
            data=[
                [P(text, p_c_bold_style) for text in ('№', 'Услуги', 'Ед.', 'Цена', 'Кол-во', 'Стоимость')],
                *(
                    [P(t, p) for t in (
                        str(i + 1), m.name, m.unit, num_to_str(m.price), num_to_str(count), num_to_str(m.price * count)
                    )]
                    for i, (m, count) in enumerate(services)
                ),
                [P('Общая стоимость:', p_r_style), '', '', '', '',
                 P(num_to_str(s_total := sum(m.price * count for m, count in services)), p)],
            ],
            style=[
                ('GRID', (0, 0), (-1, -1), 0, colors.black),
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(233 / 255, 233 / 255, 233 / 255)),
                ('SPAN', (0, -1), (-2, -1)),
            ],
            colWidths=col_width(.05, .44, .1, .11, .12, .17),
            spaceAfter=data.SPACE_AFTER,
        ),
        Table(  # header
            data=[[P(f"Сумма заказа: {num_to_str(m_total + s_total)}", h_r_style)]],
            spaceAfter=data.SPACE_AFTER
        ),
    ]

    copy = story.copy()
    pdf.build(story)
    # noinspection PyTypeChecker
    pdf.build(copy, canvasmaker=lambda *_, **__: draw_scheme(
        filename=pdf_path,
        pagesize=[
            A4[0] - p3.width,
            p3.height + data.MARGIN * 2 + t1._height + p2.height + data.SPACE_AFTER * 3
        ],
        order=order,
        ph=t1._height + p2.height + data.SPACE_AFTER * 3,
        fragments_info=False,
        _pos_y_start=A4[1] - (t1._height + p2.height + data.SPACE_AFTER * 3 + data.MARGIN),
        full_page_width=A4[0],
        fragments_numbers=False
    ))
    return pdf_path
