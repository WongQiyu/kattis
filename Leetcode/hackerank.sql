select c.company_code, c.founder,
       count(distinct l.lead_manager_code),
       count(distinct s.senior_manager_code),
       count(distinct m.manager_code),
       count(distinct e.employee_code)
from Company as c
join Lead_Manager as l
on c.company_code = l.company_code
join Senior_Manager as s
on l.lead_manager_code = s.lead_manager_code
join Manager as m
on m.senior_manager_code = s.senior_manager_code
join Employee as e
on e.manager_code = m.manager_code
group by c.company_code, c.founder
order by c.company_code;

select round(lat_n,4) from (
select row_number() over( order by lat_n asc) as rnk, lat_n from station) a
where rnk = (select Round( count(*) / 2) from station )

SELECT
  CASE
    WHEN GRADES.GRADE >= 8 THEN STUDENTS.NAME
    WHEN GRADES.GRADE < 8 THEN NULL
  END AS NAME,
  GRADES.GRADE,
  STUDENTS.MARKS
FROM STUDENTS
  LEFT JOIN GRADES ON STUDENTS.MARKS >= MIN_MARK
  AND STUDENTS.MARKS <= MAX_MARK
ORDER BY
  GRADES.GRADE DESC, STUDENTS.NAME ASC, STUDENTS.MARKS ASC;

SELECT s.name
FROM students s
JOIN friends f ON f.id = s.id
JOIN packages p1 ON s.id = p1.id
JOIN packages p2 ON f.friend_id = p2.id
WHERE p1.salary < p2.salary
ORDER BY p2.salary


SELECT profile_id, contract_id, SUM(hours_worked) as total_hours_worked
FROM activities
WHERE start_dt >= <start_dt> AND end_dt <= <end_dt>
GROUP BY profile_id, contract_id;