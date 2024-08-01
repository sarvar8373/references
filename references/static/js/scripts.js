document.addEventListener("DOMContentLoaded", function () {
  const menuItems = document.querySelectorAll(".menu-item");
  const contents = document.querySelectorAll(".content");

  menuItems.forEach(function (item) {
    item.addEventListener("click", function (event) {
      event.preventDefault();

      const target = item.getAttribute("data-target");

      // Remove active class from all contents
      contents.forEach(function (content) {
        content.classList.remove("active");
      });

      // Add active class to the target content
      const targetContent = document.getElementById(target);
      if (targetContent) {
        targetContent.classList.add("active");
      }
    });
  });
});
