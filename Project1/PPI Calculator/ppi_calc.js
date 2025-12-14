// Data structure for resolution presets
const RESOLUTIONS = {
    'hd': { width: 1280, height: 720 },
    'fhd': { width: 1920, height: 1080 },
    'qhd': { width: 2560, height: 1440 },
    // 2K is often used interchangeably with QHD in consumer electronics
    '2k': { width: 2560, height: 1440 }, 
    '4k': { width: 3840, height: 2160 },
    // UHD is technically 4K standard
    'uhd': { width: 3840, height: 2160 },
    '5k': { width: 5120, height: 2880 }
};

// 1. New Function: Apply Resolution Preset
function applyResolution(selectElement) {
    const presetKey = selectElement.value;
    
    if (presetKey === "") {
        // Preset set to -- CUSTOM --, no action needed on inputs
        return;
    }
    
    const resolution = RESOLUTIONS[presetKey];
    if (resolution) {
        // Update Width
        const widthInput = document.getElementById('width');
        const widthSlider = document.getElementById('width_slider');
        widthInput.value = resolution.width;
        widthSlider.value = resolution.width;

        // Update Height
        const heightInput = document.getElementById('height');
        const heightSlider = document.getElementById('height_slider');
        heightInput.value = resolution.height;
        heightSlider.value = resolution.height;
        
        // Automatically calculate PPI after applying a preset
        calculatePPI();
    }
}

// 2. New Function: Reset Preset Dropdown
function resetPreset() {
    // When the user manually changes width or height, reset dropdown to 'CUSTOM'
    document.getElementById('resolution-preset').value = "";
}

// 3. Existing Function: Sync Range Slider to Number Input
function updateNumber(slider) {
    const numberId = slider.id.replace('_slider', '');
    document.getElementById(numberId).value = slider.value;
    
    // Check if the change was to width or height, and reset preset
    if (numberId === 'width' || numberId === 'height') {
        resetPreset();
    }
    
    // Automatically recalculate PPI on slider/number change
    calculatePPI(); 
}

// 4. Existing Function: Sync Number Input to Range Slider
function updateSlider(numberInput) {
    const sliderId = numberInput.id + '_slider';
    document.getElementById(sliderId).value = numberInput.value;
    
    // Automatically recalculate PPI on slider/number change
    calculatePPI();
}

// 5. Existing Function: Core Calculation
function calculatePPI() {
    const width = parseFloat(document.getElementById('width').value);
    const height = parseFloat(document.getElementById('height').value);
    const diagonal = parseFloat(document.getElementById('diagonal').value);

    // Validate inputs
    if (isNaN(width) || isNaN(height) || isNaN(diagonal) || diagonal <= 0) {
        document.getElementById('result-output').textContent = "ERROR: INPUT";
        document.getElementById('result-output').style.color = "#ff0000"; 
        return;
    }

    // P = sqrt(w^2 + h^2) / d
    const diagonalResolution = Math.sqrt(width * width + height * height);
    const ppi = diagonalResolution / diagonal;

    document.getElementById('result-output').style.color = "#00ff00"; 
    document.getElementById('result-output').textContent = ppi.toFixed(2);
}

// Initial calculation on load for default values
window.onload = calculatePPI;

