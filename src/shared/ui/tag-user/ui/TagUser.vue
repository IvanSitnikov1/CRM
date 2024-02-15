<template>
    <article class="tag-user">
        <div class="tag-user__avatar">
            <img
                src="@/shared/assets/test.png"
                alt="avatar"
                class="tag-user__image"
            >
        </div>
        <Title
            class="tag-user__name"
            :data="{
                title: data.fullName,
                size: 'small',
                isHighLeading: true,
            }"
        />
        <IconBase
            v-if="data.isShowClose"
            :data="{
                iconName: 'close',
            }"
        />
    </article>
</template>

<script setup lang="ts">
import { IconBase } from '@/shared/ui/icon-base';
import { Title } from "@/shared/ui/title";
import type { ITagUser } from "@/shared/ui/tag-user";


const props = defineProps<{
  data: ITagUser
}>()
</script>

<style lang="scss">
 @import "styles.module";
</style>
