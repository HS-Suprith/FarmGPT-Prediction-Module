fertilizer_dic = {
    'Nlow': """<div class="container">
    <div class="card">
        <div class="card-body">
            <h4 class="card-title" style="color: #d9534f;">Nitrogen Deficiency (N)</h4>
            <p class="card-text">The N value of your soil is low. Nitrogen is crucial for leaf growth and green color.</p>
            <h5 class="card-subtitle mb-2 text-muted">Suggestions:</h5>
            <ul class="list-group list-group-flush">
                <li class="list-group-item"><b>1. Add Composted Manure:</b> Rich in nitrogen and organic matter.</li>
                <li class="list-group-item"><b>2. Use Nitrogen-Rich Fertilizers:</b> Apply NPK fertilizers with a high first number (e.g., 20-5-5). Urea is also a high-nitrogen option.</li>
                <li class="list-group-item"><b>3. Plant Nitrogen-Fixing Cover Crops:</b> Legumes like peas, beans, and clover pull nitrogen from the air and add it to the soil.</li>
                <li class="list-group-item"><b>4. Use Coffee Grounds:</b> Mix used coffee grounds into your soil. They are a good source of nitrogen as they decompose.</li>
                <li class="list-group-item"><b>5. Apply Grass Clippings or Mulch:</b> Using fresh grass clippings as mulch can add nitrogen to the soil.</li>
            </ul>
        </div>
    </div>
</div>""",

    'NHigh': """<div class="container">
    <div class="card">
        <div class="card-body">
            <h4 class="card-title" style="color: #5cb85c;">Nitrogen Surplus (N)</h4>
            <p class="card-text">The N value of your soil is high. Excess nitrogen can promote weed growth and harm fruit development.</p>
            <h5 class="card-subtitle mb-2 text-muted">Suggestions:</h5>
            <ul class="list-group list-group-flush">
                <li class="list-group-item"><b>1. Add Carbon-Rich Materials:</b> Mix sawdust or fine woodchips into the soil. Carbon helps absorb and tie up excess nitrogen.</li>
                <li class="list-group-item"><b>2. Plant Heavy Feeders:</b> Grow plants that consume a lot of nitrogen, such as corn, cabbage, broccoli, and tomatoes.</li>
                <li class="list-group-item"><b>3. Water Thoroughly:</b> Soaking the soil can help leach excess nitrogen deeper, away from the plant roots. Use this method carefully to avoid runoff.</li>
                <li class="list-group-item"><b>4. Avoid Adding Nitrogen:</b> Do not use nitrogen-rich fertilizers or fresh manure for a while.</li>
                <li class="list-group-item"><b>5. Do Nothing (Temporarily):</b> If you already have plants with lush green foliage, let them use up the excess nitrogen naturally.</li>
            </ul>
        </div>
    </div>
</div>""",

    'PHigh': """<div class="container">
    <div class="card">
        <div class="card-body">
            <h4 class="card-title" style="color: #5cb85c;">Phosphorus Surplus (P)</h4>
            <p class="card-text">The P value of your soil is high. High phosphorus can interfere with the uptake of other micronutrients.</p>
            <h5 class="card-subtitle mb-2 text-muted">Suggestions:</h5>
            <ul class="list-group list-group-flush">
                <li class="list-group-item"><b>1. Avoid Manure and Compost:</b> These often contain high levels of phosphorus.</li>
                <li class="list-group-item"><b>2. Use Phosphorus-Free Fertilizer:</b> Look for fertilizers where the middle number is 0 (e.g., 10-0-10).</li>
                <li class="list-group-item"><b>3. Plant Nitrogen-Fixing Legumes:</b> Use crops like beans and peas to increase nitrogen without adding more phosphorus.</li>
                <li class="list-group-item"><b>4. Use Crop Rotation:</b> Rotate with crops that are heavy phosphorus feeders to help deplete the excess over time.</li>
                <li class="list-group-item"><b>5. Water Deeply:</b> Liberal watering can help move some phosphorus out of the root zone, but use this as a last resort.</li>
            </ul>
        </div>
    </div>
</div>""",

    'Plow': """<div class="container">
    <div class="card">
        <div class="card-body">
            <h4 class="card-title" style="color: #d9534f;">Phosphorus Deficiency (P)</h4>
            <p class="card-text">The P value of your soil is low. Phosphorus is essential for root development, flowering, and fruiting.</p>
            <h5 class="card-subtitle mb-2 text-muted">Suggestions:</h5>
            <ul class="list-group list-group-flush">
                <li class="list-group-item"><b>1. Apply Bone Meal:</b> A fast-acting organic source of phosphorus.</li>
                <li class="list-group-item"><b>2. Use Rock Phosphate:</b> A slower-acting source that provides phosphorus over time.</li>
                <li class="list-group-item"><b>3. Use High-Phosphorus Fertilizers:</b> Apply fertilizers where the middle number is high (e.g., 10-20-10).</li>
                <li class="list-group-item"><b>4. Add Organic Compost or Manure:</b> These are excellent natural sources of phosphorus.</li>
                <li class="list-group-item"><b>5. Check Soil pH:</b> Phosphorus is most available to plants when the soil pH is between 6.0 and 7.0. Adjust pH if necessary.</li>
            </ul>
        </div>
    </div>
</div>""",

    'KHigh': """<div class="container">
    <div class="card">
        <div class="card-body">
            <h4 class="card-title" style="color: #5cb85c;">Potassium Surplus (K)</h4>
            <p class="card-text">The K value of your soil is high. Excess potassium can interfere with the uptake of magnesium and calcium.</p>
            <h5 class="card-subtitle mb-2 text-muted">Suggestions:</h5>
            <ul class="list-group list-group-flush">
                <li class="list-group-item"><b>1. Leach the Soil:</b> Loosen the soil and water it thoroughly multiple times, allowing it to dry in between. This helps wash out excess water-soluble potassium.</li>
                <li class="list-group-item"><b>2. Stop Using Potassium-Rich Fertilizers:</b> Avoid fertilizers where the last number is high. Use fertilizers with a '0' in the last position (e.g., 10-10-0).</li>
                <li class="list-group-item"><b>3. Balance with Calcium:</b> Add sources of calcium like crushed eggshells or gypsum to balance the nutrient ratio.</li>
                <li class="list-group-item"><b>4. Avoid Wood Ash:</b> Do not add wood ash to your soil, as it is very high in potassium.</li>
            </ul>
        </div>
    </div>
</div>""",

    'Klow': """<div class="container">
    <div class="card">
        <div class="card-body">
            <h4 class="card-title" style="color: #d9534f;">Potassium Deficiency (K)</h4>
            <p class="card-text">The K value of your soil is low. Potassium is vital for overall plant health, disease resistance, and water regulation.</p>
            <h5 class="card-subtitle mb-2 text-muted">Suggestions:</h5>
            <ul class="list-group list-group-flush">
                <li class="list-group-item"><b>1. Apply Potash Fertilizers:</b> Use Sulphate of Potash or Muriate of Potash.</li>
                <li class="list-group-item"><b>2. Use Kelp Meal or Seaweed:</b> These are excellent organic sources of potassium.</li>
                <li class="list-group-item"><b>3. Add Wood Ash:</b> Use wood ash sparingly, as it will also raise the soil pH.</li>
                <li class="list-group-item"><b>4. Bury Banana Peels:</b> Burying banana peels a few inches below the soil surface can provide a slow release of potassium.</li>
                <li class="list-group-item"><b>5. Use Sul-Po-Mag:</b> This provides potassium, sulfur, and magnesium.</li>
            </ul>
        </div>
    </div>
</div>""",
    
    'Balanced': """<div class="container">
    <div class="card">
        <div class="card-body" style="text-align: center;">
            <h4 class="card-title" style="color: #337ab7;">Nutrient Levels are Balanced</h4>
            <p class="card-text" style="font-size: 1.1rem;">Your soil nutrient levels are perfectly balanced for this crop.</p>
            <p class="card-text" style="color: #4CAF50; font-weight: bold; font-size: 1.2rem;">No fertilizer is needed at this time. Great job!</p>
        </div>
    </div>
</div>"""
}