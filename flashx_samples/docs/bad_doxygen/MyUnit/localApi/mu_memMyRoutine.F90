!> 
!!
!! 
!!
!! @file

! FORMATTING RULES
!
! Analogous to those for the MyUnit_myRoutine stub.

!> @ingroup MyUnitPrivate
!! @anchor mu_memMyRoutine_stub
!!
!! @brief <Add in one-line description>
!! 
!! @details
!! This section should be written following the same rules for the details
!! section of the MyUnit_myRoutine stub.
!!
!! @param a   My a argument
!! @param b   My b argument
!! @param c   My c argument
subroutine mu_memMyRoutine(a, b, c)
    implicit none

    ! NOTE: The full argument details are *not* included in the @param above
    ! because Doxygen can parse the code to autmatically determine such details.
    integer, intent(OUT)            :: a
    real,    intent(INOUT)          :: b
    real,    intent(IN),   optional :: c

    ...
end subroutine mu_memMyRoutine
