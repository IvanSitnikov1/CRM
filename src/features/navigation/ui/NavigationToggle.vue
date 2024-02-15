<template>
    <article
        class="logo"
        @click="app.toggleShowMenu()"
    >
        <img
            class="logo__image"
            src="@/shared/assets/specialIcons/logo.svg"
            alt="logo"
        >
    </article>
</template>

<script setup lang="ts">
import { useAppModel } from '@/entities/app';

const app = useAppModel();

</script>


<style lang="scss">
@import "style.module";
</style>

