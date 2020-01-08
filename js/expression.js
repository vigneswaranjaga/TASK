function operation(array){
    var result= findResult(array);
    console.log("Here the Output");
    return result;
    
      function findResult(input){
        var valueOne=checkComplexity(input[0]);
        var valueTwo=checkComplexity(input[2]);
        var final;
        switch(input[1]){
          case 'Plus':
            final = valueOne+valueTwo;
           break;
          case 'Minus':
            final = valueOne-valueTwo;
           break;
          case 'Times':
            final = valueOne*valueTwo;
           break;
          case 'Divide':
            final = valueOne/valueTwo;
           break;
          default:
           break;
        }
        return final;
        }
  
      function checkComplexity(value){
        return (Array.isArray(value))? findResult(value):value}
    }
  