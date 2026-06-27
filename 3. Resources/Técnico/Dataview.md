
```dataview
TABLE file.mday AS "Última modificación", type
FROM "" AND -"Plantillas" AND -"Diario"
WHERE file.mday < date(today) - dur(60 days)
SORT file.mday ASC
```


```dataview
table type as TIPO, project 
where type = "project"
```

