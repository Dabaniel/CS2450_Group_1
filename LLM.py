from gradio_client import Client

client = Client("https://b90d-161-28-242-155.ngrok-free.app/")
result = client.predict(
		"How are you?",	# str  in 'Message' Textbox component
		'LLM Chat',	# Literal[Query Docs, Search in Docs, LLM Chat]  in 'Mode' Radio component
		["https://github.com/gradio-app/gradio/raw/main/test/test_files/sample_file.pdf"],	# List[filepath]  in 'Upload File(s)' Uploadbutton component
		"Chatbot",	# str  in 'System Prompt' Textbox component
							api_name="/chat"
)
print(result)