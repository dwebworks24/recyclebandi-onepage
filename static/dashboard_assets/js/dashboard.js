$(function () {


  // =====================================
  // Profit
  // =====================================
  var chart = {
    series: [
      { name: "Earnings this month:", data: [355, 390, 300, 350, 390, 180, 355, 390] },
      { name: "Expense this month:", data: [280, 250, 325, 215, 250, 310, 280, 250] },
    ],

    chart: {
      type: "bar",
      height: 345,
      offsetX: -15,
      toolbar: { show: true },
      foreColor: "#adb0bb",
      fontFamily: 'inherit',
      sparkline: { enabled: false },
    },


    colors: ["#5D87FF", "#49BEFF"],


    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: "35%",
        borderRadius: [6],
        borderRadiusApplication: 'end',
        borderRadiusWhenStacked: 'all'
      },
    },
    markers: { size: 0 },

    dataLabels: {
      enabled: false,
    },


    legend: {
      show: false,
    },


    grid: {
      borderColor: "rgba(0,0,0,0.1)",
      strokeDashArray: 3,
      xaxis: {
        lines: {
          show: false,
        },
      },
    },

    xaxis: {
      type: "category",
      categories: ["16/08", "17/08", "18/08", "19/08", "20/08", "21/08", "22/08", "23/08"],
      labels: {
        style: { cssClass: "grey--text lighten-2--text fill-color" },
      },
    },


    yaxis: {
      show: true,
      min: 0,
      max: 400,
      tickAmount: 4,
      labels: {
        style: {
          cssClass: "grey--text lighten-2--text fill-color",
        },
      },
    },
    stroke: {
      show: true,
      width: 3,
      lineCap: "butt",
      colors: ["transparent"],
    },


    tooltip: { theme: "light" },

    responsive: [
      {
        breakpoint: 600,
        options: {
          plotOptions: {
            bar: {
              borderRadius: 3,
            }
          },
        }
      }
    ]


  };

  var chart = new ApexCharts(document.querySelector("#chart"), chart);
  chart.render();


  // =====================================
  // Breakup
  // =====================================
  var breakup = {
    color: "#adb5bd",
    series: [38, 40, 25],
    labels: ["2022", "2021", "2020"],
    chart: {
      width: 180,
      type: "donut",
      fontFamily: "Plus Jakarta Sans', sans-serif",
      foreColor: "#adb0bb",
    },
    plotOptions: {
      pie: {
        startAngle: 0,
        endAngle: 360,
        donut: {
          size: '75%',
        },
      },
    },
    stroke: {
      show: false,
    },

    dataLabels: {
      enabled: false,
    },

    legend: {
      show: false,
    },
    colors: ["#5D87FF", "#ecf2ff", "#F9F9FD"],

    responsive: [
      {
        breakpoint: 991,
        options: {
          chart: {
            width: 150,
          },
        },
      },
    ],
    tooltip: {
      theme: "dark",
      fillSeriesColor: false,
    },
  };

  var chart = new ApexCharts(document.querySelector("#breakup"), breakup);
  chart.render();



  // =====================================
  // Earning
  // =====================================
  var earning = {
    chart: {
      id: "sparkline3",
      type: "area",
      height: 60,
      sparkline: {
        enabled: true,
      },
      group: "sparklines",
      fontFamily: "Plus Jakarta Sans', sans-serif",
      foreColor: "#adb0bb",
    },
    series: [
      {
        name: "Earnings",
        color: "#49BEFF",
        data: [25, 66, 20, 40, 12, 58, 20],
      },
    ],
    stroke: {
      curve: "smooth",
      width: 2,
    },
    fill: {
      colors: ["#f3feff"],
      type: "solid",
      opacity: 0.05,
    },

    markers: {
      size: 0,
    },
    tooltip: {
      theme: "dark",
      fixed: {
        enabled: true,
        position: "right",
      },
      x: {
        show: false,
      },
    },
  };
  new ApexCharts(document.querySelector("#earning"), earning).render();
})




var counter = 1;
function addProductField() {
  var waste_obj = $('#waste_obj').val()
  var waste_list = JSON.parse(waste_obj);
  var container = document.getElementById("dynamicFieldsContainer");
  var newRow = document.createElement("div");
  newRow.className = "row mt-3";
  newRow.id = "row_" + counter;
  var materialId = "wast_id_" + counter;
  var materialPrice = "price_" + counter;
  var materialPercentage = "quantity_" + counter;

  newRow.innerHTML = `
    <div class="col-sm-12 col-md-6 col-lg-3">
      <label for="${materialId}" class="form-label">Waste Type</label>
      <select class="form-select" id="${materialId}" name="wast_id" aria-label="Waste type select">
        <option selected>Open this select menu</option>
    
      </select>
    </div>
    <div class="col-sm-12 col-md-3 col-lg-3">
        <label for="${materialPrice}" class="form-label">Price</label>
      <input type="text" class="form-control" id="${materialPrice}" name="price_1" placeholder="Please enter price" aria-label="price">
    </div>
    <div class="col-sm-12 col-md-6 col-lg-3">
      <label for="${materialPercentage}" class="form-label">Quantity</label>
      <input type="text" class="form-control" id="${materialPercentage}" name="quantity" placeholder="Please enter quantity" aria-label="Quantity">
    </div>
    <div class="col-sm-12 col-md-6 col-lg-3 my-auto">
      <button type="button" class="btn btn-primary mt-5 add-row-btn" onclick="addProductField()">+ADD</button>
      <button type="button" class="btn btn-danger mt-5" onclick="removeProductField('row_${counter}')">-REMOVE</button>
      </div>
  `;

  container.appendChild(newRow);
  var selectElement = document.getElementById(materialId);
  waste_list.forEach(function(material) {
      var option = document.createElement("option");
      option.text = material.fields.wastename;
      option.value = material.pk;
      selectElement.appendChild(option);
  });


  $(document).ready(function() {
    $('#materialId').select2({
        placeholder: "Select Material",
        theme: "bootstrap5",
        width: "100%" 
    });
});

 
  counter++;
}


function removeProductField(rowId) {
  var row = document.getElementById(rowId);
  row.parentNode.removeChild(row);
}



// add shop owner

function saveshopowner(){
  const first_name = $("#first_name").val();
  const last_name = $("#last_name").val();
  const email = $("#email").val();
  const phone = $("#phone").val();
  const shop_name = $("#shop_name").val();
  const shopType = $('#shop_type').val();
  const area = $("#area").val();
  const city = $("#city").val();
  const state = $("#state").val();
  const zip_code = $("#zip_code").val();
  const rcbAgreement = $('input[name="rcb_agreement"]:checked').val();
 

    $.ajax({
      url: '/save_shop/',
      method: 'POST',
      data: {
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'phone':phone,
        'shop_name':shop_name,
        'shopType':shopType,
        'area':area,
        'city':city,
        'state':state,
        'zip_code':zip_code,
        'rcbAgreement':rcbAgreement,
      },
      success: function(response){
        x = response
        show_success(response['message'])
        window.location = response['path']
      },
      error: function(response){
        show_error(response.responseJSON['error'])
      }
    })
}