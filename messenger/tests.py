from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread, Message

# Create your tests here.
class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'test1234')
        self.user2 = User.objects.create_user('user2', None, 'test1234')
        self.user3 = User.objects.create_user('user3', None, 'test1234')
        #Para cada ttest independiente se ejecuta de nuevo el setUp, por lo tanto, debemos agregar los usuarios en cada test que hagamos

        self.thread = Thread.objects.create()
#Añadir usuarios y mensajes


    def test_add_users_to_thread(self): #Añadir usuarios
        self.thread.users.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.users.all()), 2) #Comprueba si dos valores son equivalentes
    #Comprueba la longitud(2 usuarios) en el hilo

    def test_filter_thread_by_users(self):
        self.thread.users.add(self.user1, self.user2)
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2) #Obtiene todos los hilos donde forma parte el usuario 1 , añadiendo otro filtro podemos obtener todos los hilos del usuario 2. Como es un QuerySet podemos agregar tantos filtros como desearamos
        self.assertEqual(self.thread, threads[0])
    #Recupera un hilo ya existentet a partir de sus usuarios

    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(len(threads), 0)
    #Comprueba de que no existe un hilo cuando los usuarios no forman parte de el

    def test_add_messages_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Hola")
        message2 = Message.objects.create(user=self.user2, content="Tienes sueno?")
        self.thread.messages.add(message1, message2)
        self.assertEqual(len(self.thread.messages.all()), 2)

        #ver conversacion
        for message in self.thread.messages.all():
            print("({}): {}".format(message.user, message.content))
    #Agregar mensajes al hilo

    def test_add_message_from_user_not_in_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Hola")
        message2 = Message.objects.create(user=self.user2, content="Como andas?")
        message3 = Message.objects.create(user=self.user3, content="Un  cansado")
        self.thread.messages.add(message1, message2, message3)
        self.assertEqual(len(self.thread.messages.all()), 2)
    #Comprobar si un usuario que no forma parte del hilo puede agregar algun mensaje