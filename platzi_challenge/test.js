function interest(money, perc, period) {
  let semester = (money*(perc/100)) + money
  console.log(`Esto generaste en 1 semestre:  $ ${semester.toFixed(2)}`)
      for(i = 1; i < period; i++) {
          semester += (semester*(perc/100))
          console.log(`Esto generaste en ${i + 1} semestres: $ ${semester.toFixed(2)}`)
      }
}

interest(100, 4, 6)