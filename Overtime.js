
// calculates salary that is earned via regular time and overtime
function overtime(startTime ,  endTime,salary  ,overtimePerc ){
  // if someone has worked earlier than 9 am or later than 12 pm terminate
  if (startTime > endTime || startTime < 9 || endTime > 24){
    return;
  }

  // is the end time of work regular, so at 5 pm?
  let isEndTimeReg = endTime <= 17;
  // the overtime salary is a product of the regular salary and the overtime percentage
  const  overtimeSalary = (salary * overtimePerc);

  // calculate regular hours
  let hours = !(isEndTimeReg) ? 17 - startTime : endTime - startTime;
  // calculate overtime hours
  let overtimeHours =   !(isEndTimeReg) ? endTime - 17  :  0;

  // sum of regular and overtime salary each
  let totalSalary = hours * salary + overtimeHours * overtimeSalary ;

 return totalSalary;
}

console.log("sala", overtime(13.25, 15, 30, 1.5))
