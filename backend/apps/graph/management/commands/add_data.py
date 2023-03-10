# import sqlite3
# from django.core.management.base import\
#     BaseCommand, CommandParser
# from graph.models import Node, Growth


# DATABASE_NAME = 'CN-Agro.db'


# class Command(BaseCommand):
#     help = 'Move data from CN-Agro.sb to career.sqlite3'
    
#     def handle(self, *args, **options) -> None:
#         connection = sqlite3.connect(DATABASE_NAME)
#         self.cursor = connection.cursor()

#         self.cursor.execute('SELECT * FROM professions')
#         professions = self.cursor.fetchall()
#         for profession in professions:
#             code, name, node_type, counter = profession
#             Node.objects.create(
#                 name=name,
#                 node_type=node_type,
#                 counter=counter,
#                 code=code
#             )

#         self.cursor.execute("SELECT * FROM growths")
#         growths = self.cursor.fetchall()
        
#         for growth in growths:
#             _, first_node_id, second_node_id, period, counter = growth
#             start_node = Node.objects.get(code=first_node_id)
#             end_node = Node.objects.get(code=second_node_id)
#             Growth.objects.create(
#                 start_node=start_node,
#                 end_node=end_node,
#                 counter=counter,
#                 period=period
#             )
        
#         for node in Node.objects.all():
#             node.code = -1
#             node.save()
