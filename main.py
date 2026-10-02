def SKU_generator(e):
document.______________('sku_output').innerHTML = " "
category = document.getElementById('________').value
__________ = document.getElementById('___________').value
stock_qty = document.getElementById('quantity').value
sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(________)
display("SKU: ", sku, target='___________')
def create_order(e):
# Get input values
prod1 = document.getElementById("item1")
prod2 = document.getElementById("item2")
prod3 = document.getElementById("item3")
prod4 = document.getElementById("item4")
prod5 = document.getElementById("item5")
# Calculate total by multiplying value by checked status (1 or 0)
# Calculate subtotal, tax, and total
_________ = (float(prod1.value) * prod1.checked +
float(prod2.value) * prod2.checked +
float(prod3.value) * prod3.checked +
float(prod4.value) * prod4.checked +
float(prod5.value) * prod5.checked)
tax_rate = 0.12 # 12% VAT, no need for excise tax. too complicated
tax = subtotal __ tax_rate
total = subtotal __ tax
# display(f"==== Receipt ==== <br> Subtotal: ₱ {subtotal:.2f} ", target="show")
# display(f"Subtotal: ₱ {subtotal:.2f} ", target="show")
# display(f"VAT: ₱ {tax:.2f} ", target="show")
# display(f"Total: ₱ {total:.2f} ", target="show")
receipt = f"""
<h3>==== Receipt ====</h3>
<p>Subtotal: ₱{subtotal:.2f}</p>
<p>Tax: ₱{tax:.2f}</p>
<p><strong>Total: ₱{total:.2f}</strong></p>
"""
document.getElementById("show")._____________= receipt # use this instead of display to avoid displaying the HTML tags