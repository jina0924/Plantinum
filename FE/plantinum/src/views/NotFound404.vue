<template>
    <div class="home">
        <div class="wrapper">
            <router-link class="plantinum" :to="{ name: 'home' }">Plantinum</router-link>

            <div class="text1">
                <p>잘못된 요청입니다</p>
            </div>
            <div class="btn1">
                <router-link :to="{ name: 'home' }">
                    <button class="btn">돌아가기</button>
                </router-link>
            </div>
            <div class="forzerofor">
                <p>404</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "NotFound404"
}
</script>

<style scoped>
.home {
    background-image: url(../assets/404/blue-shelf-mockup-with-product-presentation3d-rendering.jpg);
    background-size: cover;
    display: flex;
    flex-direction: column;
    align-items: center;
    /* width: 100%; */
    /* height: 100%; */
    height: 100vh;
    margin: 0;
}

.wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
}

.plantinum {
    font-family: 'Dancing Script', cursive;
    color: black;
    font-size: 2.5rem;
    margin-top: 50%;
    margin-bottom: 10%;
}

.text1 {
    font-size: 1rem;
    font-family: 'SUIT', sans-serif;
    font-weight: bold;
}

.btn {
    border-radius: 5px;
    border: 0;
    height: 35px;
    font-size: 1rem;
    background-color: #b2c9ab;
    color: white;
    width: 6rem;
    align-items: center;
    margin-bottom: 0;
}

.btn1:hover {
    background-color: #65805d;
    color: #ffffff;
}

.forzerofor {
    font-family: 'SUIT', sans-serif;
    font-size: 10rem;
    font-weight: bold;
    color: white;
    text-shadow: 2px 2px 5px rgba(16, 39, 112, .2);
    /* background-color: #65805d; */
    align-items: center;
    margin-bottom: 50%;
}
</style>
