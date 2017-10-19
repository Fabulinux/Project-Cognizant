process.stdin.resume();
process.stdin.setEncoding("ascii");
var input = "";
process.stdin.on("data", function (chunk) {
    input += chunk;
});
process.stdin.on("end", function () {
    var fibonacciList = input.split(" "); // Split the input
    var val = '';
    var termToCheck = newInput.pop(); // extract the number to check
    var index = fibonacciList.length-1; // get initial location
    
    // change array from input string to ints
    for(var i = 0; i<fibonacciList.length;i++){
        fibonacciList[i] = parseInt(fibonacciList[i]);
    }
    
    // while current fibbonacci list has not reached the nth term
    while(fibonacciList.length < termToCheck){
        index = fibonacciList.length-1;
        val = fibonacciList[index-1] + Math.pow(fibonacciList[index],2); // Calculate
        fibonacciList.push(val); // push to list
    }
    console.log(fibonacciList.pop());
});
