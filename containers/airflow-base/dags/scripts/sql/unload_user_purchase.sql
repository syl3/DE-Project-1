COPY (
    select invoice_number,
        stock_code,
        detail,
        quantity,
        invoice_date,
        unit_price,
        customer_id,
        country
    from retail.user_purchase
    where invoice_date between '{{ execution_date.date() }}' and '{{ (execution_date + macros.timedelta(days=1)).date() }}' -- we should have a date filter here to pull only required data
) TO '{{ params.user_purchase }}' WITH (FORMAT CSV, HEADER);