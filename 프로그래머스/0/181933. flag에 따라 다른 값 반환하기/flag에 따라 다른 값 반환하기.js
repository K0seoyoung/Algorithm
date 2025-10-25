function solution(a, b, flag) {
    let trueAnswer = a + b;
    let falseAnswer = a - b;
    
    if(flag) {
        return trueAnswer;
    } else{
        return falseAnswer;
    }
}