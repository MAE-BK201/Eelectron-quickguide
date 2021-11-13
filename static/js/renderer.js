async function increment() {
  const counterElement = document.getElementById("counter");

  counterElement.innerText = await eel.increment_from_python(
    counterElement.innerText
  )();
}
