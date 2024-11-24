alter table public."order"
    add guide_decor_2 smallint;


SELECT "order".create_date::text AS date,
       customer.name             AS customer,
       concat("user".number, repeat('0'::text, 3 - length("order".number::text)), "order".number::text,
              CASE
                  WHEN order_number_part.number IS NOT NULL THEN concat(' (', order_number_part.number::text, ')')
                  ELSE ''::text
                  END)           AS number,
       profile.name              AS profile,
       "order".description,
       "order".id
FROM "order"
         JOIN customer ON "order".customer_id = customer.id
         JOIN "user" ON "order".responsible_user_id = "user".id
         JOIN profile ON "order".profile_id = profile.id
         LEFT JOIN order_number_part ON order_number_part.order_id = "order".id