# Lola
Asistente Virtual para Raspberry Pi totalmente en español.

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
	
	6. Otras funciones: responde a preguntas básicas com saludos y despedidas.
	
## Requisitos para instalar en raspberry pi.
	- Módulo python SpeechRecognition para el STT.
	- Módulo python de Telegram para la interacción con el bot.
	- Paquete PicoTTS.
	- Módulo python wikipedia para la consulta de información (pendiente de prescindir).
