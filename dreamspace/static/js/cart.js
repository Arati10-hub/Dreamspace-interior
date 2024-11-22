function updateQuantity(operation,productId)
{
   const inputBox=document.getElementById("quantity"+productId);
   inputBox.value=parseInt(inputBox.value)+operation;
}