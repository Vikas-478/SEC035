function createPyramid() {
  const letters = ['A', 'B', 'C', 'D', 'E'];
  const levels = 5;

  for (let i = 0; i < levels; i++) {
    if (i === 2) {
      continue;
    }

    let level = '';

    for (let j = 0; j < levels - i - 1; j++) {
      level += ' ';
    }

    for (let k = 0; k <= i; k++) {
      level += letters[k] + ' ';
    }

    console.log(level);
  }
}

createPyramid();