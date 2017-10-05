from peewee import Model, SqliteDatabase, CharField, IntegerField

sqlite_db = SqliteDatabase('trucks.db')

class BaseModel(Model):
    class Meta:
        database = sqlite_db


class Persona(Model):
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    edad = IntegerField(null=True)

# crear tablas
sqlite_db.create_tables([Persona], safe=True)

# crear persona
p = Persona()
p.nombre = "pepe"
p.apellido = "lui"
p.save()


for i in range(9):
    p = Persona()
    p.nombre = "pepe_" + str(i)
    p.apellido = "lui_" + str(i)
    p.save()
    print "persona", p.id


# QUERYS

todos = Persona.select()
filtrado = Persona.select().where(Persona.nombre.endswith("7"))

# borrado
for dato in filtrado:
    dato.delete_instance()



