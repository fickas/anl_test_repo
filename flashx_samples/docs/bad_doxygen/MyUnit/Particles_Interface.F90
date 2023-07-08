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

! FORMATTING RULES
!
! Analogous to those for the Particles_myRoutine stub.

!> @ingroup Particles
!! @anchor Particles_simpleGeneric_int_stub
!!
!! @brief Integer version of @ref particles_interface::particles_simplegeneric "Particles_simpleGeneric generic interface"
!! 
!! @details
!! This section should be written following the same rules for the details
!! section of the Particles_myRoutine stub and should establish the contract for
!! all versions of this generic interface.
!!
!! @param a   My a argument
!! @param b   My b argument
subroutine Particles_simpleGeneric_int(a, b)
    implicit none

    ! NOTE: The full argument details are *not* included in the @param above
    ! because Doxygen can parse the code to automatically determine such details.
    integer, intent(IN)  :: a
    real,    intent(OUT) :: b

    ...
end subroutine Particles_simpleGeneric_int