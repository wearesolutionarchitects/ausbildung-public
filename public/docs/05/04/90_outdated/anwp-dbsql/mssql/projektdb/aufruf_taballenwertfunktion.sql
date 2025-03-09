SELECT 
        projects.project_name AS Projektname,
        SUM(DATEDIFF(MINUTE, task_start_time, task_end_time)) AS Arbeitszeit_in_Minuten,
        SUM(DATEDIFF(MINUTE, task_start_time, task_end_time) / 60.0) AS Arbeitszeit_in_Stunden,
        SUM(DATEDIFF(MINUTE, task_start_time, task_end_time) / 60.0) * employee_hourly_rate AS Kosten
    FROM tasks
    INNER JOIN projects ON tasks.projects_id = projects.projects_id
    INNER JOIN employee ON tasks.employee_id = employee.employee_id
    INNER JOIN employee_hourly_rate ON employee.employee_hourly_rate_id = employee_hourly_rate.employee_hourly_rate_id
    WHERE projects.projects_id = 1
    GROUP BY projects.project_name, employee_hourly_rate