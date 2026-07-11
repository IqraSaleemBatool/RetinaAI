// ===============================
// RetinaAI Dashboard Script
// ===============================

// Image Preview
const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");

if (imageInput) {
    imageInput.addEventListener("change", function () {

        const file = this.files[0];

        if (file) {

            const reader = new FileReader();

            reader.onload = function (e) {

                preview.src = e.target.result;

            }

            reader.readAsDataURL(file);

        }

    });
}

// ===============================
// Analyze Button (Dummy Prediction)
// ===============================

const analyzeBtn = document.querySelector(".analyze-btn");

if (analyzeBtn) {

    analyzeBtn.addEventListener("click", function () {

        if (!imageInput.files.length) {

            alert("Please upload a retinal image first.");

            return;

        }

        analyzeBtn.innerHTML =
            '<i class="fa-solid fa-spinner fa-spin"></i> Analyzing...';

        analyzeBtn.disabled = true;

        // Simulate AI Processing
        setTimeout(function () {

            document.getElementById("disease").innerText =
                "Diabetic Retinopathy";

            document.getElementById("confidence").innerText =
                "94.2%";

            document.getElementById("severity").innerText =
                "Moderate";

            // Update Progress Bars
            const progress = document.querySelectorAll("progress");

            progress[0].value = 3;
            progress[1].value = 94;
            progress[2].value = 1;
            progress[3].value = 1;
            progress[4].value = 1;

            // AI Explanation
            document.querySelectorAll(".card p")[6].innerHTML =
                `
                The uploaded retinal image shows
                <b>microaneurysms</b> and
                <b>retinal hemorrhages</b>,
                which are commonly associated with
                <b>Diabetic Retinopathy</b>.
                The confidence score is high,
                therefore further clinical examination
                by an ophthalmologist is recommended.
                `;

            // RAG Section
            document.querySelectorAll(".card ul")[0].innerHTML = `
                <li><b>Description:</b> Diabetes damages retinal blood vessels.</li>
                <li><b>Symptoms:</b> Blurred vision, floaters, vision loss.</li>
                <li><b>Risk Factors:</b> Diabetes, hypertension, obesity.</li>
                <li><b>Treatment:</b> Anti-VEGF injections, laser therapy.</li>
                <li><b>Reference:</b> American Academy of Ophthalmology.</li>
            `;

            analyzeBtn.innerHTML =
                '<i class="fa-solid fa-check"></i> Analysis Complete';

            analyzeBtn.style.background = "#198754";

        }, 2000);

    });

}

// ===============================
// Sidebar Active Menu
// ===============================

const menuItems = document.querySelectorAll(".sidebar li");

menuItems.forEach(item => {

    item.addEventListener("click", function () {

        menuItems.forEach(i => i.classList.remove("active"));

        this.classList.add("active");

    });

});

// ===============================
// Hover Animation for Cards
// ===============================

const cards = document.querySelectorAll(".card");

cards.forEach(card => {

    card.addEventListener("mouseenter", function () {

        card.style.transform = "translateY(-6px)";

    });

    card.addEventListener("mouseleave", function () {

        card.style.transform = "translateY(0px)";

    });

});

// ===============================
// Current Date in History (Optional)
// ===============================

const today = new Date();

console.log("RetinaAI Dashboard Loaded");

console.log(today.toDateString());

// ===============================
// Future Functions
// ===============================

// uploadImage()

// predictDisease()

// generateGradCAM()

// retrieveKnowledge()

// generateLLMExplanation()

// savePrediction()

// loadHistory()