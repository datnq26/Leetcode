-- Write your PostgreSQL query statement below
select p.product_id, p.product_name from Product as p left join Sales as s on p.product_id = s.product_id group by p.product_id, p.product_name having min(sale_date) >= '2019-01-01' and max(sale_date) <= '2019-03-31';
