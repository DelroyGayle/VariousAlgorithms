function chain_longest(pivot, words) {
    let new_words = [pivot];
    let lastchar = pivot[pivot.length-1];
    
    for (let word of words) {
        let potential_words = [];
        for (let searchword of words) {
            if (searchword[0] === lastchar && new_words.indexOf(searchword) < 0) {
                potential_words.push(searchword);
            }
        }
        
        if (potential_words.length) {
            potential_words.sort((a, z) => a.length - z.length);
            let next_word = potential_words[0];
            new_words.push(next_word);
            pivot = next_word;
            lastchar = pivot[pivot.length-1];
        }
    }

    return new_words;
}

const getMax = (a, b) => a.length >= b.length ? a : b;

function find_longest(words) {
  
  let all_chains =  words.map((element, _, array) => chain_longest(element, array));
  if (!all_chains.length) {
    return [];
  }
  
  return all_chains.reduce(getMax);  
  
}

let words = ['giraffe', 'elephant', 'ant', 'tiger', 'racoon', 'cat', 'hedgehog', 'mouse'];
console.log(find_longest(words));
// ['hedgehog', 'giraffe', 'elephant', 'tiger', 'racoon']

words = [];
console.log(find_longest(words));
// []

words = ['apple', 'orange', 'eggplant', 'pear', 'hop', 'tooth', 'zaza'];
console.log(find_longest(words));
// ['zaza', 'apple', 'eggplant', 'tooth', 'hop', 'pear']

words = ['dog', 'giraffe', 'elephant', 'ant', 'tiger', 'racoon', 'cat', 'hedgehog', 'mouse'];
console.log(find_longest(words));
// [ 'dog', 'giraffe', 'elephant', 'tiger', 'racoon' ]

words = [
    'apple', 'orange', 'pear', 'pineapple', 
    'durian', 'grapes', 'banana', 'kiwi',
    'dragonfruit', 'coconut', 'starfruit', 'strawberry',
    'acai', 'cherry', 'papaya', 'peach',
    'lychee', 'lemon', 'olive', 'tomato',
    'cherry tomato', 'elderberry', 'yuzu', 'avocado'
]
console.log(find_longest(words));
// [ 'grapes', 'starfruit', 'tomato', 'olive', 'elderberry', 'yuzu' ]
