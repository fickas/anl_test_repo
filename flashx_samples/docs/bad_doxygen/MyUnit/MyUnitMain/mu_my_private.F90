!> @copyright Copyright 2022 UChicago Argonne, LLC and contributors
!!
!! @licenseblock
!! Licensed under the Apache License, Version 2.0 (the "License");
!! you may not use this file except in compliance with the License.
!!
!! Unless required by applicable law or agreed to in writing, software
!! distributed under the License is distributed on an "AS IS" BASIS,
!! WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
!! See the License for the specific language governing permissions and
!! limitations under the License.
!! @endlicenseblock
!!
!! @file
!!
!! @brief Private implementation - non-stubbed.
!! 
!! @details
!! Adds 2 numbers
!!
!! @param a - a number
!! @param b - a number
subroutine mu_my_private(a, b, c)
    implicit none

    integer, intent(IN)            :: a
    integer, intent(IN)            :: b
    integer, intent(OUT)           :: c
    
    c = a+b
end subroutine mu_my_private

