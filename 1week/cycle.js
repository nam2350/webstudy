let bikes = [];

function FindBikeStaion(count) {

    for(let i = 0; i < bikes.length; i ++) {

        let bikeCount = bikes[i]['parkingBikeToCnt'];
        let bikeStation = bikes[i]['stationName'];

        if( bikeCount < count ) {
            console.log(bikeStation);
        }
    }
}