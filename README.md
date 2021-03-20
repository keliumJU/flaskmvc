# flaskmvc
refactoring de un proyecto en python con el framework flask, donde el objetivo es convertir la estructura basica de flask en un proyecto completo utilizando el patron de arquitectura 
mvc para construir un api rest, ademas de implementar patrones de dinsenio como el singleton y dto.
Como es un proyecto de ejemplo la logica del negocio es un CRUD comun.

-Se recomienda instalar un entorno virtual. se utiliza sqlAlchemy como ORM para acceder a la base de datos Mysql 



endpoints:


metodo post(para aniadir una tabla)
http://127.0.0.1:1234/mysql_engine/table

{
    "name":"lpm",
    "campos":[
        {"field":"id","type_column":"INT(6) UNSIGNED","key":"PRIMARY KEY","null_column":"","default":"","extra":"AUTO_INCREMENT"},
        {"field":"firstname","type_column":"VARCHAR(30)","null_column":"NOT NULL","key":"","default":"","extra":"" }
    ]
}

metodo put(para actualizar una tabla por nombre)
http://127.0.0.1:1234/mysql_engine/table

{ 
    "name":"lpm", 
    "campos":
    [
        {"field":"id","type_column":"INT(6) UNSIGNED","key":"PRIMARY KEY","null_column":"","default":"","extra":"AUTO_INCREMENT"},
        {"field":"other","type_column":"VARCHAR(56)","null_column":"","key":"","default":"DEFAULT 'LPM NOTHING'","extra":"" },
        {"field":"other2","type_column":"VARCHAR(56)","null_column":"","key":"","default":"DEFAULT 'LPM NOTHING'","extra":"" } 
    ]
 }

metodo get(listar todas las bases de datos)
http://127.0.0.1:1234/mysql_engine


metodo post(crear la base de datos)
http://127.0.0.1:1234/mysql_engine/

{
    "name":"dataname"
}


metodo get(listar tablas y columnas)
http://127.0.0.1:1234/mysql_engine/all


metodo get(para usar base de datos(selecciona))
http://127.0.0.1:1234/mysql_engine/<nombre_database>


