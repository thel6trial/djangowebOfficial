import AosModule from './modules/AosModule.js';
import CountDownModule from './modules/CountDownModule.js';
import CounterModule from './modules/CounterModule.js';
import CourseModule from './modules/CourseModule.js';
import FixedToolsModule from './modules/FixedToolsModule.js';
import FlatPickrModule from './modules/FlatPickrModule.js';
import FormatPhoneNumber from './modules/FormatPhoneNumber.js';
import HeaderDropdownModule from './modules/HeaderDropdownModule.js';
import HeaderFixedModule from './modules/HeaderFixedModule.js';
import HeaderModule from './modules/HeaderModule.js';
import LightGalleryModule from './modules/LightGalleryModule.js';
import MfpModule from './modules/MfpModule.js';
import ScrollToSectionModule from './modules/ScrollToSectionModule.js';
import ScrollToTopModule from './modules/ScrollToTopModule.js';
import SearchFilterModule from './modules/SearchFilterModule.js';
import SearchModule from './modules/SearchFilterModule.js';
import SwiperModule from './modules/SwiperModule.js';
import TabModule from './modules/TabModule.js';
import ViewportModule from './modules/ViewportModule.js';

$(document).ready(function ($) {
  AosModule()
  CountDownModule();
  CounterModule();
  CourseModule()
  FixedToolsModule();
  FlatPickrModule();
  FormatPhoneNumber()
  HeaderDropdownModule();
  HeaderFixedModule();
  HeaderModule();
  LightGalleryModule();
  MfpModule();
  ScrollToSectionModule()
  ScrollToTopModule();
  SwiperModule();
  TabModule();
  ViewportModule();
  SearchModule();
  SearchFilterModule();
});
