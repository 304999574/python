$(function(){
	            $("#btnShow").click(function(){
                $.ajax({
                    url: "03-stockbuy",
                    type: "get",
                    data: {
                        stockcode: $("#input1").val(),
                        starttime: $("#sdate").val(),
                        endtime: $("#edate").val()
                    },
                    async: true,
                    dataType: "json",
                    success: function (data) {
                        Stockname = data[data.length - 1];
                        var listdata = [];
                        for (var i = 0; i < data.length - 1; i++) {
                            var daydata = data[i];

                            listdata.push(daydata)
                        }
                    }
                })
                })
})
