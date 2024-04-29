/*
    Write a function factorial(n) that takes in a positive integer n, 
    and returns the product of 1 to n ie. 1 * 2 * 3 * ... * n
*/

function factorial(n) {
    if (n<=1)
          return n;
    else 
          return n * factorial(n - 1);
  }
  
  console.log(factorial(10))