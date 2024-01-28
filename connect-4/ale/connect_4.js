let get_board = () => [
  [0, 0, 0, 0, 0, 0, 0], // bottom
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0], // top
];

const assert = (condition, message) => {
  if (!condition)
    throw Error('Assert failed: ' + (message || ''));
};

let display = (board) => {
  process.stdout.write('----\n');
  for (const row of board) {
    for (const cell of row) {
      process.stdout.write(cell.toString());
    }
    process.stdout.write('\n');
  }
}

let check_winner = (row, column, board) => {
  player = board[row][column];
  // check the column
  if (row > 2) {
    let matching = 1;
    for (let i = row - 1; i >= 0; i--) {
      if (board[i][column] !== player) {
        break;
      }
      matching += 1;
    }
    if (matching >= 4) {
      return true;
    }
  }
  // check the row
  matching = 1;
  for (let j = column - 1; j >= 0; j--) {
    if (board[row][j] !== player) {
      break;
    }
    matching += 1;
  }
  for (let j = column + 1; j < board[row].length; j++) {
    if (board[row][j] !== player) {
      break;
    }
    matching += 1;
  }
  if (matching >= 4) {
    return true;
  }
  // check the tl-br diagonal
  matching = 1;
  for (let i = row - 1, j = column - 1; i >= 0 && j >= 0; i--, j--) {
    if (board[i][j] !== player) {
      break;
    }
    matching += 1;
  }
  for (let i = row + 1, j = column + 1; i < board.length && j < board[0].length; i++, j++) {
    if (board[i][j] !== player) {
      break;
    }
    matching += 1;
  }
  if (matching >= 4) {
    return true;
  }
  // check the bl-tr diagonal
  matching = 1;
  for (let i = row + 1, j = column - 1; i < board.length && j >= 0; i++, j--) {
    if (board[i][j] !== player) {
      break;
    }
    matching += 1;
  }
  for (let i = row - 1, j = column + 1; i >= 0 && j < board[0].length; i--, j++) {
    if (board[i][j] !== player) {
      break;
    }
    matching += 1;
  }
  if (matching >= 4) {
    return true;
  }
  matching = 1;

  return false;
}

let drop = (player, column, board) => {
  row = undefined;
  for (let i = 0; i < board.length; i++) {
    if (board[i][column] === 0) {
      board[i][column] = player;
      row = i;
      break;
    }
  }
  return row;
}

let run = () => {
  // node.js readline: https://stackoverflow.com/a/68504470/5239250
  const readline = require('readline');

  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  const prompt = (query) => new Promise((resolve) => rl.question(query, resolve));

  (async() => {

    let board = get_board();
    for (let i = 0; i < board.length * board[0].length; i++) {
      const player = 1 + i % 2;
      display(board);
      let column = await prompt(`Player ${player}, column: `);
      row = drop(player, parseInt(column), board);
      if (row === undefined) {
        console.log(`Column overflow`);
      } else if (check_winner(row, column, board)) {
        display(board);
        console.log(`Player ${player} has won!`);
        break;
      }

    }
    rl.close()
  })();

  rl.on('close', () => process.exit(0));

}

let run_tests = () => {
  // TODO: redo the test by setting the 1 and 2 in the array rather than using drop
  {
    // check four in a column
    board = get_board()
    board[0][2] = 1;
    board[1][2] = 1;
    let row = drop(1, 2, board);
    assert(row === 2, 'third coin on row 2')
    let won = check_winner(row, 2, board);
    assert(won === false, 'do not win with three coins in a column');
    row = drop(1, 2, board)
    won = check_winner(row, 2, board);
    assert(won === true, 'do win with three coins in a column');
    display(board);
  }
  {
    // check four in a row
    board = get_board()
    board[0][1] = 1;
    board[0][2] = 1;
    let row = drop(1, 4, board);
    assert(row === 0, 'first coin on row 4')
    let won = check_winner(row, 2, board);
    assert(won === false, 'do not win with 2 + 1 coins in a row');
    row = drop(1, 3, board);
    won = check_winner(row, 2, board);
    assert(won === true, 'win with 4 coins in a row');
    display(board);
  }
  {
    // check the tl - br diagonal
    board = get_board()
    board[0][0] = 1;
    board[0][1] = 2;
    board[1][1] = 1;
    board[0][2] = 2;
    board[1][2] = 2;
    board[0][3] = 2;
    board[1][3] = 2;
    board[2][3] = 2;
    let row = drop(1, 3, board);
    let won = check_winner(row, 3, board);
    display(board);
    assert(won === false, 'do not win before the diagonal has 4');
    row = drop(1, 2, board);
    won = check_winner(row, 2, board);
    display(board);
    assert(won === true, 'win on the diagonal');
  }
  {
    // check the bl - tr diagonal
    board = get_board()
    board[0][0] = 2;
    board[1][0] = 2;
    board[2][0] = 2;
    board[3][0] = 1;
    board[0][1] = 2;
    board[1][1] = 2;
    board[2][1] = 1;
    board[0][2] = 2;
    let row = drop(1, 3, board);
    let won = check_winner(row, 3, board);
    display(board);
    assert(won === false, 'do not win before the diagonal has 4');
    row = drop(1, 2, board);
    won = check_winner(row, 2, board);
    display(board);
    assert(won === true, 'win on the diagonal');
  }
}

// run_tests();
run()
