# Lola
Asistente Virtual para Raspberry Pi totalmente en español.

## Novedades de la versión 1.0
	- Añadidos nuevos módulos como: definiciones, traductor, reproductor de música local...
	- Corrección de bugs menores.

## Para funcionar completamente, el asistente utiliza:
	- El sistema STT de Google (versión de prueba, con limitaciones).
	- El bot de telegram "LolaVA".
	- El sistem TTS PicoTTS de Linux.
	- Bases de datos externas, para obtener información.
	
## La versión actual del programa contiene los siguientes módulos (con una o más funciones):
	1. Tiempo: dice la hora.
	Ejemplo: "Lola, ¿puedes decirme la hora?".
  
	2. Clima: utiliza la API de openweathermap.org para devolver la información del tiempo por ciudades.
	Ejemplo: "¿Cómo es el clima en Reykjavik?".

	3. Noticias: utiliza la RSS de los 4 periódicos más leídos en España (El País, El Mundo, La Vanguardia y ABC) para obtener información.
	Ejemplo: "¿Cuáles son las notícias destacadas de hoy?".

	4. Wikipedia: consulta información en wikipedia.org.
	Ejemplo: "¿Quién es Santi Balmes?".
	Ejemplo: "Me gustaría saber qué es el Mar Mediterraneo".
	Ejemplo: "¿Cuál es la capital de Portugal?"
	
	5. Calculadora: devuelve el resultado de diferentes operaciones matemáticas (suma, resta, multiplicación, división, raíz y potencia). Para utilizar la función, la consulta debe empezar con la palabra "calcular".
	Ejemplo: "Calcular 15 menos 12".
	Ejemplo: "Calcular 4 elevado a 6".
	Ejemplo: "Calcular raíz 3 de 27".
	
	6. Conversación: responde a preguntas o demandas concretas con respuestas concretas
	Ejemplo: "¿Conoces algún chiste?"

	7. Alarma: permite programar una alarma con un mensaje personalizado.
	Ejemplo: "Quiero configurar una nueva alarma".
	
	8. Diccionario: busca definiciones de palabras en la web Wikitionary.org (Página creada por los creadores de wikipedia, no está completa).
	Ejemplo: "Definición de silla".
	
	9. Traductor: detecta el idioma y traduce al castellano una frase introducida.
	Ejemplo: "Traducir 'the less I know the better'".
	
	10. Reproductor de música local: reproduce música de un dispositivo USB.
	Ejemplo: "Quiero escuchar música".
	
## Requisitos para instalar en raspberry pi.
	- Tener instalado ALSA Sound para linux.
	- Módulo python SpeechRecognition para el STT.
	- Módulo python de Telegram para la interacción con el bot.
	- Paquete PicoTTS.
	
## Otros recursos utilizados.
	- Sonido de inicio: https://freesound.org/s/131659
	- Sonido de final de frase: https://freesound.org/s/131662
