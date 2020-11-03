# Select Queries Here

# 1) user table
select_user_by_id = "SELECT * FROM user WHERE uid=?"
select_all_users = "SELECT * FROM user"


# 2) customer table
select_cust_by_id = "SELECT * FROM customer WHERE cid=?"
select_all_cust = "SELECT * FROM customer"


# 3) employee table
select_emp_by_id = "SELECT * FROM employee WHERE eid=?"
select_all_emp = "SELECT * FROM employee"


# 4) role table
select_role_by_id = "SELECT * FROM role WHERE rid=?"
select_all_role = "SELECT * FROM role"


# 5) subscription table
select_subs_by_id = "SELECT * FROM subscription WHERE sid=?"
select_all_subs = "SELECT * FROM subscription"


# 6) tarrif_plan table
select_plan_by_id = "SELECT * FROM tarrif_plan WHERE pid=?"
select_all_plan = "SELECT * FROM tarrif_plan"


# 7) usage table
select_usage_by_id = "SELECT * FROM usage WHERE sid=?"
select_all_usage="SELECT * FROM usage"

# 8) customer_bill table
select_bill_by_sid = "SELECT * FROM customer_bill WHERE sid=?"
select_bill_by_cid = "SELECT * FROM customer_bill WEHERE cid=?"
total_bill_cost_for_cid = "SELECT SUM(total_cost) FROM customer_bill WHERE cid=?"

# 9) VIEW : [subscription_by_customer] usage details - for customer
select_all_usage_details = "SELECT * FROM [subscriptions_by_customer]"
select_usage_details_by_sid = "SELECT * FROM [subscriptions_by_customer] where sid=?"
select_usage_details_by_cid = "SELECT * FROM [subscriptions_by_customer] where cid=?"

# 10) VIEW: [bill_details_per_sub]subscription details  - for operator
select_all_subs_details = "SELECT * FROM [bill_details_per_sub]"
select_subs_details_by_sid = "SELECT * FROM [bill_details_per_sub] where sid=?"
select_subs_details_by_cid = "SELECT * FROM [bill_details_per_sub] where cid=?"
