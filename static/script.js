// Count how many symptoms are selected
const checkboxes = document.querySelectorAll("input[type='checkbox']");
const counter = document.getElementById("counter");

checkboxes.forEach(box => {
  box.addEventListener("change", () => {
    const checked = document.querySelectorAll("input[type='checkbox']:checked").length;
    counter.textContent = `Selected: ${checked} symptom${checked !== 1 ? 's' : ''}`;
  });
});
