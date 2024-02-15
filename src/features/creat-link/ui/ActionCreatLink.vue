<template>
    <ActionButton
        @click="handlerTest"
        :data="{
            iconName: 'search',
            color: '#15C0E6',
        }"
    />
</template>

<script setup lang="ts">
import { ActionButton } from '@/shared/ui/action-button';
import { useCustomWebNotification } from '@/shared/lib/ustils/notification';

const { isSupported, show: showNotification } = useCustomWebNotification();

const handlerTest = () => {
  if (isSupported.value) {
    showNotification({
      title: 'Custom Notification',
      body: 'Create Test User!'
    });
  }
};

</script>

<style lang="scss">
  @import "style.module";
</style>
