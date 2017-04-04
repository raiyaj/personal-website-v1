$(document).ready(function() {

  var expression = "";
  var currentExpr = "";

  $("button").on("click", function(e) {
      var elem = e.target.innerHTML;  //eg. the button's value (string)

      var digits = "0123456789";
      var operators = "÷×+-";
      if (digits.indexOf(elem) !=  -1) {  //digit
        if (elem == "0") { //0
          if (currentExpr.length > 1 || (currentExpr.length == 1 && operators.indexOf(currentExpr) == -1)) {
          expression += elem;
          currentExpr += elem;  //only add the 0 if it's not the first digit in current expression
          }
        } else {  //digit 1 to 9
          expression += elem;
          if (currentExpr.length == 1 && operators.indexOf(currentExpr) != -1) {
            currentExpr = elem;
          } else {
            currentExpr += elem;
          }
        }
      } else if (elem == "." && currentExpr.indexOf(".") == -1) { //decimal point, and no other decimal point exists in current expression
        if (currentExpr.length == 0 || (currentExpr.length == 1 && operators.indexOf(currentExpr) != -1)) { //add a 0 before the decimal if it's the first char in currentExpr, or if first char is an operator
          expression += "0" + elem;
          currentExpr = "0" + elem; //get rid of operator
        } else {
          expression += elem;
          currentExpr += elem;
        }
      } else if (operators.indexOf(elem) != -1 && operators.indexOf(expression[expression.length-1]) == -1  && expression.length != 0) {  //eg. if button is an operator and last character in expression isn't an operator and first character of expression is also a digit
        expression += elem;
        currentExpr = elem;
        console.log("hello?");
      } else if (elem == "AC") {  //AC button clears entire expression
        expression = "";
        currentExpr = "";
      } else if (elem == "CE") {  //CE button only clears current expresison

        var foundCurrentExpr = false;
        var cutoff;
        var i = expression.length - currentExpr.length;
        while (foundCurrentExpr === false) {
          if (expression[i] === currentExpr[0]) {
            cutoff = i;
            foundCurrentExpr = true;
          }
          i -= 1;
        }
        console.log(cutoff);

        var exprMinusCurrent = "";
        for (var i=0;i<cutoff;i++) {  //construct new string, copy of original expression up to cutoff
          exprMinusCurrent += expression[i];
        };
        expression = exprMinusCurrent;  //set expression equal to new string
        if (currentExpr.length != 0 && operators.indexOf(currentExpr) != -1) {
          //allow to continue adding to prev number if you CE off an operator
          var doesOperatorExist = false;
          for (var l=0;l<expression.length;l++) {
            if (operators.indexOf(expression[l]) != -1) {
              doesOperatorExist = true;
            }
          }
          if (doesOperatorExist == true) {
            var foundCeOperator = false;  //flag
            var j = expression.length-1;
            var ceOperatorPos;
            while (foundCeOperator == false) {
              if (operators.indexOf(expression[j]) != -1) {
                foundCeOperator = true;
                ceOperatorPos= j;
              }
              j -= 1;
            };
            //console.log(ceOperatorPos);
            var middleChunkExpr = "";
            for (var k=ceOperatorPos+1;k<expression.length;k++) {
              middleChunkExpr += expression[k];
            }
            currentExpr = middleChunkExpr;
            //console.log(currentExpr);
          } else {
            currentExpr = expression;
          }
        } else {
          currentExpr = "";
        }
      }


      //What to actually display when each button is clicked
      var result = "";
      var formattedResult = "";


      if (elem == "AC") {
        $("h2").html("0");
        $("p").html("0");

      } else if (elem == "CE") {
        $("h2").html("0");
        if (expression == "") {  //needed when expression consists of only 1 term and becomes an empty string when CE button clicked
          $("p").html("0");
        } else {
          $("p").html(expression);
        }

      } else if (elem == "=" && expression != "") { //2nd condition prevents an error if equal button pressed twice in a row
        var translatedExpression = "";
        for (var i=0;i<expression.length;i++) {  //translate expression into one readable by eval() by replacing ÷ with / and × with *
          if (expression[i] == "÷") {
            translatedExpression += "/";
          } else if (expression[i] == "×") {
            translatedExpression += "*";
          } else {
            translatedExpression += expression[i];
          }
        }

        //round result to max 3 decimal places
        result = eval(translatedExpression);
        result = Math.round(result*1000)/1000;

        //display evaluated expression, but reset variables
        $("h2").html(result);
        formattedResult = expression + "=" + result;
        $("p").html(formattedResult);
        expression = "";
        currentExpr = "";
        console.log(result);

      } else {
        if (expression == "") {   //needed when elem was not accepted above (eg. a 0 or operator at beginning)
          $("h2").html("0");
          $("p").html("0");
        } else {
          if (currentExpr == "") {
            $("h2").html("0");
            $("p").html(expression);
          } else {
            $("h2").html(currentExpr);
            $("p").html(expression);
          }
        }
      }

      //console.log(expression);
      //console.log(currentExpr);

      //Display msg when oveflow is reached and reset variables
      if (expression.length > 22 || formattedResult.length > 22 || currentExpr.length > 9 || result.toString().length > 9) {
        $("h2").html("0");
        $("p").html("Digit Limit Met");
        expression = "";
        currentExpr = "";
      }



  });
});
