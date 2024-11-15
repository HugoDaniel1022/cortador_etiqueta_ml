import fitz  # PyMuPDF

# Abre el PDF existente
pdf_document = fitz.open("prueba.pdf")

# Crea un nuevo documento PDF
new_pdf = fitz.open()

# Define las coordenadas del área que deseas conservar (sin el encabezado)
rect = pdf_document[0].rect  # Obtiene el rectángulo de la primera página
# Ajusta las coordenadas (x0, y0, x1, y1) según tus necesidades
x0 = 0        # Coordenada x inicial
y0 = 100     # Coordenada y inicial (ajusta según la altura del encabezado)
x1 = rect.width  # Coordenada x final (ancho de la página)
y1 = rect.height  # Coordenada y final (alto de la página original)

# Crea un nuevo rectángulo con las coordenadas ajustadas
new_rect = fitz.Rect(x0, y0, x1, y1)

# Crea una nueva página en el nuevo PDF
new_page = new_pdf.new_page(width=new_rect.width, height=new_rect.height)

# Copia el contenido de la parte recortada de la página original a la nueva página
new_page.show_pdf_page(new_page.rect, pdf_document, 0, keep_proportion=True, clip=new_rect)

# Guarda el nuevo PDF
new_pdf.save("etiqueta_ml.pdf")
new_pdf.close()
pdf_document.close()
