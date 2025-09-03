from pypdf import PdfReader, PdfWriter

# File paths
main_pdf = "main.pdf"
functions_pdf = "Functions.pdf"
electricity_pdf = "Electricity.pdf"
statics_pdf = "Statics.pdf"
dynamics_pdf = "Dynamics.pdf"
output_pdf = "final.pdf"

# Create a PdfWriter object
writer = PdfWriter()

# Add the first 3 pages of main.pdf
main_reader = PdfReader(main_pdf)
for page in main_reader.pages[:3]:
    writer.add_page(page)

# Add all pages of Functions.pdf
functions_reader = PdfReader(functions_pdf)
for page in functions_reader.pages:
    writer.add_page(page)

# Add the rest of the pages of main.pdf (from page 4 onwards)
for page in main_reader.pages[3:]:
    writer.add_page(page)

# Add all pages of Electricity.pdf
electricity_reader = PdfReader(electricity_pdf)
for page in electricity_reader.pages:
    writer.add_page(page)

# Add all pages of Statics.pdf
statics_reader = PdfReader(statics_pdf)
for page in statics_reader.pages:
    writer.add_page(page)

# Add all pages of Dynamics.pdf
dynamics_reader = PdfReader(dynamics_pdf)
for page in dynamics_reader.pages:
    writer.add_page(page)

# Write the final merged PDF to output file
with open(output_pdf, "wb") as output_file:
    writer.write(output_file)

print(f"Merged PDF created successfully as {output_pdf}")