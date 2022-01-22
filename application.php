<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> CANDIDACY</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
    <link rel="stylesheet" href="css/application.css">
</head>

<body>
    <div class="sheet">
        <div class="a">
            <img src="images/usg.png" width="150px" height="150px">
        </div>
        <div class="b">
            <p> APPLICATION FOR CANDIDACY </p>
        </div>
    </div>
    <form action="">
        <div class="mid">
            <form>
                <div class="form-row">
                    <div class="form-group col-md-6">
                        <label for="firstname">FIRSTNAME</label>
                        <input type="email" class="form-control" id="firstname">
                    </div>
                    <div class="form-group col-md-6">
                        <label for="surname">SURNAME</label>
                        <input type="text" class="form-control" id="surname">
                    </div>
                </div>
                <div class="form-row">
                    <div class="form-group col-md-7">
                        <label for="cs">COURSE & SECTION</label>
                        <input type="text" class="form-control" id="cs">
                    </div>
                    <div class="form-group col-md-2">
                        <label for="gender">Gender</label>
                        <select id="inputState" class="gender">
                    <option selected>select</option>
                        <option>Female</option>
                        <option>Male</option>
                    </select>
                    </div>
                    <div class="form-group col-md-3">
                        <label for="age">AGE</label>
                        <input type="text" class="form-control" id="age">
                    </div>
                </div>
                <div class="form-row">
                    <div class="form-group col-md-6">
                        <label for="pos">POSITION</label>
                        <input type="text" class="form-control" id="pos">
                    </div>
                    <div class="form-group col-md-6">
                        <label for="party">PARTYLIST</label>
                        <input type="text" class="form-control" id="party">
                    </div>
                </div>
            </form>
            <div class="pic">
                <input id="aaa" type="file" accept="images/*">
            </div>
        </div>
        <div class="huli">
            <div class="nn">
                <label for="desc">DESCRIBE YOURSELF</label>
                <textarea name="desc" id="desc" cols="10" rows="50"></textarea>
            </div>
            <div class="chck">
                <input type="checkbox" id="chck">
                <label for="chck">TERMS AND CONDITION</label>
            </div>
        </div>
    </form>
    <div class="bttn">
        <a href="homepage.html" id="cancel">CANCEL</a>
        <a class="aaa" id="pindot" type="submit" name="submit">SUBMIT</a>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.min.js" integrity="sha384-VHvPCCyXqtD5DqJeNxl2dtTyhF78xXNXdkwX1CZeRusQfRKp+tA7hAShOK/B/fQ2" crossorigin="anonymous"></script>
    <script src="js/application.js"></script>


</body>

</html>