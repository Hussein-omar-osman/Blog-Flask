const btnJoke = document.getElementById('joke');
const p1 = document.getElementById('p1');
const p2 = document.getElementById('p2');
const p3 = document.getElementById('p3');

btnJoke.addEventListener('click', () => {
  getData();
});

async function getData() {
  let res = await fetch('http://quotes.stormconsultancy.co.uk/random.json');
  let data = await res.json();
  if (data) {
    // console.log(data.quote);
  } else {
    console.log('no data');
  }

  p1.innerText = data.id;
  p2.innerText = data.quote;
  p3.innerText = data.author;
  return data;
}

let obj = {
  name: 'hussein',
  age: 22,
};

console.log(obj.name);
