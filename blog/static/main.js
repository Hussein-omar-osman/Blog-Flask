const btnJoke = document.getElementById('joke');
const p2 = document.getElementById('quote');
const p3 = document.getElementById('author');

btnJoke.addEventListener('click', () => {
  getData();
});

async function getData() {
  let res = await fetch('http://quotes.stormconsultancy.co.uk/random.json');
  let data = await res.json();
  if (data) {
    console.log(data);
    p2.innerText = data.quote;
    p3.innerText = `- ${data.author} -`;
    return data;
  } else {
    console.log('no data');
  }
}

let obj = {
  name: 'hussein',
  age: 22,
};

console.log(obj.name);
