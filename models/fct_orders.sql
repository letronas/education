
select 
    payments.order_id as order_id
    , customers.customer_id as customer_id
    , payments.amount 
from {{ ref("stg_orders") }} as orders
left join {{ ref("stg_payments") }} as payments
        on orders.order_id = payments.order_id
left join {{ ref("stg_customers") }} customers
        on orders.customer_id = customers.customer_id