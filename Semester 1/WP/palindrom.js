//sum of digit and reverse of a number
let num = parseInt(prompt("Enter a number:"));
let sum = 0;
let reverse = 0;
let original = num;

while (num > 0) 
{
  let digit = num % 10;   // Get last digit
  sum += digit;           // Add to sum
  reverse = reverse * 10 + digit; // Build reverse number
  num = Math.floor(num / 10); // Remove last digit
}

alert("Sum of digits: " + sum);
alert("Reversed number: " + reverse);

if(reverse==original)
alert("Palindrom");
else
alert("Not Palindrom");
