<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>COMELEC</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
    <link rel="stylesheet" href="css/comelec.css">

</head>

<body>
    <div class="sheet">
        <div class="top">
            <div class="img">
                <img src="images/usg.png" width="200px" height="200px">
            </div>
            <div class="sulat">
                <div class="in">
                    <p> COMELEC OFFICIAL </p>
                    <p>CANDIDATE LIST</p>
                </div>
            </div>

        </div>
    </div>

    <div class="mid">
        <div class="table">
            <table id="candidates" class="table d-print-table-cell">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Firstname</th>
                        <th scope="col">Surname</th>
                        <th scope="col">Age</th>
                        <th scope="col">Course & Section</th>
                        <th scope="col">Position</th>
                        <th scope="col">Partylist</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">1</th>
                        <td>Mark</td>
                        <td>Otto</td>
                        <td>22</td>
                        <td>BSIE-ICT-2A</td>
                        <td>President</td>
                        <td>None</td>

                    </tr>
                    <tr>
                        <th scope="row">2</th>
                        <td>Jacob</td>
                        <td>Thornton</td>
                        <td>22</td>
                        <td>BSME-2A</td>
                        <td>Vice President</td>
                        <td>Manalo</td>

                    </tr>
                    <tr>
                        <th scope="row">3</th>
                        <td>Larry</td>
                        <td>Gonzales</td>
                        <td>20</td>
                        <td>BET-COET-NS-2B</td>
                        <td>President</td>
                        <td>None</td>
                    </tr>
                    <tr>
                        <th scope="row">4</th>
                        <td>Shiela</td>
                        <td>Crus</td>
                        <td>22</td>
                        <td>BSIE-ICT-3B</td>
                        <td>President</td>
                        <td>None</td>
                    </tr>
                    <tr>
                        <th scope="row">5</th>
                        <td>Ankol</td>
                        <td>Badi</td>
                        <td>25</td>
                        <td>BSIE-ICT-3A</td>
                        <td>Senator</td>
                        <td>None</td>
                    </tr>
                    <tr>
                        <th scope="row">6</th>
                        <td>Lisa</td>
                        <td>Perez</td>
                        <td>23</td>
                        <td>BSCE-3B</td>
                        <td>Treasurer</td>
                        <td>Manalo</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="btns">
        <button id="b">REMOVE</button>
        <button id="b">UPLOAD</button>
    </div>

    <div class="last">
        <a type="button" href="index.html" id="button">LOG OUT</a>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.min.js" integrity="sha384-VHvPCCyXqtD5DqJeNxl2dtTyhF78xXNXdkwX1CZeRusQfRKp+tA7hAShOK/B/fQ2" crossorigin="anonymous"></script>
    <script src="js/comelec.js"></script>

</body>

</html>