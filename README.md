# Lola
Asistente Virtual para Raspberry Pi totalmente en español.

## Novedades de la versión 0.2
	- Se ha añadido la carpeta para subprocesos, para poder ejecutar scripts en segundo plano.
	- Añadida la opción de crear alarmas.
	- Cambio entero del encoding del programa, cambiando el encoding del sistema de 'ascii' a 'utf-8'.
	- Cambios internos que hacen más legible la carpeta de configuración.
	- Corrección de bugs menores.

## Para funcionar completamente, el asistente utiliza:
	- El sistema STT de Google (versión de prueba, con limitaciones).
	- El bot de telegram "LolaVA".
	- El sistem aTTS PicoTTS de Linux.
	
## La versión actual del programa contiene los siguientes módulos (con una o más funciones):
	1. Tiempo: dice la hora.
	Ejemplo: "Lola, ¿puedes decirme la hora?".
  
	2. Clima: utiliza la API de openweathermap.org para devolver la información del tiempo por ciudades.
	Ejemplo: "¿Cómo es el clima en Reykjavik?".

	3. Noticias: utiliza la RSS de los 4 periódicos más leídos en España (El País, El Mundo, La Vanguardia y ABC) para obtener información.
	Ejemplo: "¿Cuáles son las notícias destacadas de hoy?".

	4. Wikipedia: consulta información en wikipedia.org.
	Ejemplo: "¿Quién es Santi Balmes?".
	Ejemplo: "Me gustaría saber qué es el comunismo".
	
	5. Calculadora: devuelve el resultado de diferentes operaciones matemáticas (suma, resta, multiplicación, división, raíz y potencia). Para utilizar la función, la consulta debe empezar con la palabra "operar".
	Ejemplo: "Operar 15 menos 12".
	Ejemplo: "Operar 4 elevado a 6".
	Ejemplo: "Operar raíz 3 de 27".
	
	6. Conversación: responde a preguntas o demandas concretas con respuestas concretas
	Ejemplo: "¿Conoces algún chiste?"

	7. Funciones adicionales como: alarma.
	Ejemplo: "Quiero configurar una nueva alarma"
	
## Requisitos para instalar en raspberry pi.
	- Tener instalado ALSA sound para linux.
	- Módulo python SpeechRecognition para el STT.
	- Módulo python de Telegram para la interacción con el bot.
	- Paquete PicoTTS.
	- Módulo python wikipedia para la consulta de información (pendiente de prescindir).
