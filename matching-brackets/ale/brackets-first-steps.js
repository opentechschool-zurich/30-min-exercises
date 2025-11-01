
function main() {
  let brackets = ')('

  // for (i = 0; i < brackets.length; i++) {
  //   c = brackets[i]
  // }
  //
  // for c: brackets:
  //   print(c)
  //
  let in_brackets = false
  for (let c of brackets) {
    console.log(c)
    if (c == '(') {
      in_brackets = true
    } else if (c == ')') {
      if (in_brackets == true) {
        console.log('ok');
      } else {
        console.log('ko');
        return
      }
    }
  }
}

main()
